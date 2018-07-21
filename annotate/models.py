from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField("公司全称", max_length=50, primary_key=True)
    address = models.CharField("地址", max_length=50, blank=True, null=True)
    phone = models.CharField("联系方式", max_length=20, blank=True, null=True)
    synonym = models.BooleanField("同义词库", default=False)
    # company_synonym = models.ManyToManyField(
    # CompanySynonym, verbose_name="同义词库")

    def __str__(self):
        return self.name


class CompanySynonym(models.Model):
    name = models.CharField("词条名", max_length=20)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name="公司通名")

    def __str__(self):
        return self.name


class News(models.Model):
    id = models.CharField("编号", max_length=10, primary_key=True)
    title = models.CharField("标题", max_length=70, blank=True, null=True)
    link = models.URLField(verbose_name="链接", blank=True, null=True)
    company = models.ManyToManyField(Company, verbose_name="企业", blank=True)
    tech = models.ManyToManyField("Tech", verbose_name="技术关键词", blank=True)
    finance = models.ManyToManyField(
        "Finance", verbose_name="投融资关系", blank=True)
    source = models.CharField("来源", max_length=15, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"


class Patent(models.Model):
    STATUS_CHOICES = (
        ("PUBLIC", "公开"),
        ("PRIVATE", "私有保护"),
        ("EXPIRED",  "过期"),
    )
    id = models.CharField("专利编号", max_length=20, primary_key=True)
    name = models.CharField("专利名", max_length=30, blank=True, null=True)
    author = models.CharField("著作人", max_length=20, blank=True, null=True)
    status = models.CharField("状态", max_length=10, choices=STATUS_CHOICES)
    tech = models.ManyToManyField("Tech", verbose_name="技术关键词")

    def __str__(self):
        return self.id + ":" + self.name


class Tech(models.Model):
    name = models.CharField("名称", max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class TechSynonym(models.Model):
    name = models.CharField("词条名", max_length=20)
    tech = models.ForeignKey(
        Tech, on_delete=models.CASCADE, verbose_name="技术通名")

    def __str__(self):
        return self.name


class Finance(models.Model):
    company_from = models.ForeignKey(
        Company, on_delete=models.DO_NOTHING, verbose_name="资方", related_name="capital")
    company_to = models.ForeignKey(
        Company, on_delete=models.DO_NOTHING, verbose_name="受方", related_name="recipient")
    level = models.CharField("级别", max_length=10, blank=True, null=True)
    description = models.CharField("描述", max_length=20, blank=True, null=True)

    def __str__(self):
        return self.description
    # TODO: from != to
    # TODO: 投资类型表作为外键

# 添加原生待标注的关键词表


class Keywords(models.Model):
    name = models.CharField("关键词", max_length=50)
    news = models.ManyToManyField("News", verbose_name="新闻", blank=True)
    is_labeled = models.BooleanField("是否标注", default=False)
    # patent = models.ManyToManyField("Patent", verbose_name="专利")

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class KeywordsCompany(Keywords):
    pass


class KeywordsTech(Keywords):
    patent = models.ManyToManyField("Patent", verbose_name="专利", blank=True)

    # -----------------------shell test -------------------
    # from annotate.models import Company, CompanySynonym
# from annotate.models import Company, CompanySynonym, News, Patent, Tech, TechSynonym, Finance, KeywordsCompany, KeywordsTech
