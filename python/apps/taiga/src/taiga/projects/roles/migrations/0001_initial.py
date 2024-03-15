# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2023-present Kaleidos INC

# Generated by Django 4.1.3 on 2023-06-12 18:57

import django.contrib.postgres.fields
import django.db.models.deletion
import taiga.base.db.models
import taiga.base.db.models.fields
import taiga.base.utils.datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectRole",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        blank=True,
                        default=taiga.base.db.models.uuid_generator,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="name")),
                ("slug", taiga.base.db.models.fields.LowerSlugField(blank=True, max_length=250, verbose_name="slug")),
                (
                    "permissions",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(
                            choices=[
                                ("add_story", "Add story"),
                                ("comment_story", "Comment story"),
                                ("delete_story", "Delete story"),
                                ("modify_story", "Modify story"),
                                ("view_story", "View story"),
                            ]
                        ),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                        verbose_name="permissions",
                    ),
                ),
                (
                    "order",
                    models.BigIntegerField(default=taiga.base.utils.datetime.timestamp_mics, verbose_name="order"),
                ),
                ("is_admin", models.BooleanField(default=False, verbose_name="is_admin")),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="roles",
                        to="projects.project",
                        verbose_name="project",
                    ),
                ),
            ],
            options={
                "verbose_name": "project role",
                "verbose_name_plural": "project roles",
                "ordering": ["project", "order", "name"],
            },
        ),
        migrations.AddIndex(
            model_name="projectrole",
            index=models.Index(fields=["project", "slug"], name="projects_ro_project_63cac9_idx"),
        ),
        migrations.AddConstraint(
            model_name="projectrole",
            constraint=models.UniqueConstraint(
                fields=("project", "slug"), name="projects_roles_projectrole_unique_project_slug"
            ),
        ),
        migrations.AddConstraint(
            model_name="projectrole",
            constraint=models.UniqueConstraint(
                fields=("project", "name"), name="projects_roles_projectrole_unique_project_name"
            ),
        ),
    ]
