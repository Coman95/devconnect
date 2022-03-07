from django.db import models
from django.db.models.fields import TimeField
import uuid
from users.models import Profile

from django.templatetags.static import static

# Create your models here.
class Project(models.Model):
    """Django model for Projects"""

    # Delete project when owner was deleted
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # null=True =>  value can be Null in the DB
    # blank=True => when submitting a form or post request we cannot submit with this value being blank
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)

    # '' for Tag because its defined below this model
    tags = models.ManyToManyField("Tag", blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    created = models.DateTimeField(
        auto_now_add=True
    )  # take timestamp from whenever this gets generated
    # override basic id
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        # display project as title in admin panel
        return self.title

    class Meta:
        ordering = ["-vote_ratio", "-vote_total", "title"]

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            # Set default image
            url = static("images/default.jpg")
        return url

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list("owner__id", flat=True)
        return queryset

    @property
    def getVotecount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value="up").count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()


class Review(models.Model):
    """Django model for Reviews"""

    VOTE_TYPE = (("up", "Up Vote"), ("down", "Down Vote"))
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )  # establish one to many relationship
    # whenever a project is deleted, what to do with all the children ? all reviews connected to the project
    # cascade deletes all reviews
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    #  make sure of 1 to 1 relationship
    class Meta:
        unique_together = [["owner", "project"]]

    def __str__(self):
        return self.value


class Tag(models.Model):
    """Django model for Tags"""

    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.name
