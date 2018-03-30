from django.db import models


class Comment(models.Model):
    COMMENT_TYPES = (
        ('POST', "Post comment"),
        ('PROD', "Product comment"),
        ('PORT', "Portfolio comment"),
        ('TEST', "Testimonial"),
    )

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comment_user')
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)
    category = models.CharField(max_length=24, choices=COMMENT_TYPES)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comment_post_id', blank=True, null=True)

    # TODO: Add these when product and portfolio apps are created
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    # portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)

    def __str__(self):
        return 'Comment: %s %s' % (self.id, self.category)

    def __unicode__(self):
        return self.text

    def approve(self):
        self.approved_comment = True
        self.save()