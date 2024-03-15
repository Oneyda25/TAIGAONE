# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2023-present Kaleidos INC

# Generated by Django 4.1.3 on 2023-06-12 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("projects", "0001_initial"),
        ("mediafiles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mediafile",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mediafiles",
                to="projects.project",
                verbose_name="project",
            ),
        ),
        migrations.AddIndex(
            model_name="mediafile",
            index=models.Index(fields=["object_content_type", "object_id"], name="mediafiles__object__cb24da_idx"),
        ),
        migrations.AddIndex(
            model_name="mediafile",
            index=models.Index(fields=["project"], name="mediafiles__project_e8bd81_idx"),
        ),
    ]
