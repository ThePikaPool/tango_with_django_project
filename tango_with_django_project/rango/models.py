from django.db import models
from django.template.defaultfilters import slugify

# alright, starting chapter 5. i don't have much time till this is due,
# might have to pull an all nighter

class Category(models.Model):


    name = models.CharField(max_length=128, unique=True)
    # guessing the above is making a database field that's the primary key
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
            verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Page(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # oh it's just CS1F stuff
    # bravo UofG, the preliminary courses now make sense
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
