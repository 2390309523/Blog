from django.db import models

# Create your models here.
class Style(models.Model):
    '个人主页的风格,id为1的是通用样式'
    # id:主键
    style_id = models.AutoField(primary_key = True)
    # window颜色风格
    style_windows_color = models.CharField(max_length=10,null=True,default="white")
    # window字体大小
    style_font_size = models.SmallIntegerField(default=12,null=True)
    # 字体粗细
    style_font_weight=  models.SmallIntegerField(default=400,null=True)
    def __str__(self):
        return "颜色："+self.style_windows_color

class HeadPortrait(models.Model):
    '头像'
    header_id = models.AutoField(primary_key = True)
    # 文件路径
    header_path = models.FilePathField(path='\home\jiarui\python-test\django\mysite\\blog\image')
    def __str__(self):
        return self.header_path

class User(models.Model):
    '用户'
    # 自增长字段:主键
    user_id = models.AutoField(primary_key=True)
    # 可变长字符字段：用户名，不可重复
    user_username = models.CharField(max_length=18,unique=True)
    # 密码
    user_password = models.CharField(max_length=18)
    # 用户邮箱
    user_email = models.EmailField(max_length=50,null=True)
    # 用户电话号码
    user_phone = models.CharField(max_length=20,null=True)
    # 用户昵称
    user_nickname = models.CharField(max_length=50,default=user_username)
    # 性别
    user_sex = models.CharField(max_length=2,default='男',choices=(('男','nan'),('女','nv')))
    # 用户创建的时间

    use_create_time = models.DateTimeField(auto_now_add=True)
    # 用户更新个人信息的时间
    user_update_time = models.DateTimeField(auto_now_add=True)
    # 用户个人博客的样式（外键）
    user_style = models.IntegerField(null=True,default=1)
    # 用户头像（外键）
    user_head_portrait = models.IntegerField(default=0)
    # one-one
    user_style = models.ForeignKey(to=Style , on_delete=models.SET_DEFAULT,default=1,null=True)
    # one-one
    user_head_portrait = models.ForeignKey(to=HeadPortrait,on_delete=models.SET_DEFAULT,default=1,null=True)
    def __str__(self):
        return self.user_username

class Admin(models.Model):
    '管理员，以备不时之需'
    # 管理员id：主键
    admin_id = models.AutoField(primary_key = True)
    # 管理员登录的账号
    admin_username = models.CharField(max_length=50,unique=True)
    # 密码
    admin_password = models.CharField(max_length=50,default='666666',null=True)
    # 邮箱
    admin_email = models.EmailField(null=True)
    # 管理员电话号码
    admin_phone = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.admin_username

class Blog(models.Model):
    '博客正文'
    # 博客id：主键
    blog_id = models.AutoField(primary_key = True)
    # 博客标题
    blog_title = models.CharField(max_length=100,default=None)
    # 博客作者：外键
    blog_author = models.IntegerField()
    # 博客内容
    blog_content = models.TextField(max_length=1024*5)
    # 博客标签：外键，关联到标签
    blog_lable = models.IntegerField()
    # 博客的创建时间
    blog_create_time = models.DateTimeField(auto_now_add=True,null=True)
    # 博客的更新时间
    blog_update_time = models.DateTimeField(auto_now=True,null=True)
    # 博客发布的类型（0,1,2）分别表示（私密，公开，草稿箱）
    blog_public_style = models.SmallIntegerField(default=0,choices=((0,0),(1,1),(2,2)),null=True)
    # 博客的点赞数量
    blog_like_count = models.IntegerField(default=0,null=True)
    # 博客的评论数量
    blog_comment_count = models.IntegerField(default=0,null=True)
    # 博客的浏览数量
    blog_access_count = models.IntegerField(default=0,null=True)
    # 1-n
    blog_author = models.ForeignKey(to=User,on_delete=models.CASCADE)

    def __str__(self):
        return "标题："+self.blog_title+"; 作者："+self.blog_author

class Lable(models.Model):
    '标签'
    # 标签的id
    lable_id = models.AutoField(primary_key=True)
    # 标签对应的博客id
    lable_blog_id = models.ForeignKey(to=Blog,null=True,on_delete=models.SET_NULL)
    # 标签对应的用户的id
    lable_user_id = models.ForeignKey(to=User,null=True,on_delete=models.SET_NULL)
    # 标签的内容
    lable_content = models.CharField(max_length=50)
    def __str__(self):
        return self.lable_content



class Friend(models.Model):
    '好友'
    friend_id = models.AutoField(primary_key = True)
    # 外键，对应user
    friend_n = models.IntegerField()
    # 外键，对应userid
    friend_m = models.IntegerField()
    # 好友备注
    friend_note = models.CharField(max_length=50)
    # 好友状态
    friend_status = models.SmallIntegerField(choices=((0,0),(1,1)))
    friend_n = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='friend_n')
    friend_m = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='friend_m')
    def __str__(self):
        return self.friend_note

class Comments(models.Model):
    '评论'
    comment_id = models.AutoField(primary_key = True)
    # 评论用户的id
    comment_user_id = models.IntegerField()
    # 评论文章的id
    comment_blog_id = models.IntegerField()
    # 点赞数量
    comment_like_count = models.IntegerField(default=0,null=True)
    # 评论内容
    comment_content = models.TextField(max_length=1024)
    comment_user_id = models.ForeignKey(to=User,on_delete=models.CASCADE)
    comment_blog_id = models.ForeignKey(to=Blog,on_delete=models.CASCADE)
    def __str__(self):
        return self.comment_content;