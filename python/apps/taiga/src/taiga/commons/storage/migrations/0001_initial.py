# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2023-present Kaleidos INC

# Generated by Django 4.2.3 on 2023-09-01 19:14

import django.db.models.functions.datetime
import taiga.base.db.models
import taiga.base.utils.datetime
import taiga.commons.storage.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StoragedObject",
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
                (
                    "created_at",
                    models.DateTimeField(
                        default=taiga.base.utils.datetime.aware_utcnow,
                        verbose_name="created at",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, null=True, verbose_name="deleted at"),
                ),
                (
                    "file",
                    models.FileField(
                        max_length=500,
                        upload_to=taiga.commons.storage.models.get_storaged_object_file_patch,
                        verbose_name="file",
                    ),
                ),
            ],
            options={
                "verbose_name": "storaged_objects",
                "verbose_name_plural": "storaged_objects",
                "ordering": ["-created_at"],
                "indexes": [
                    models.Index(
                        django.db.models.functions.datetime.TruncDate("created_at"),
                        models.F("created_at"),
                        name="created_at_date_idx",
                    ),
                    models.Index(
                        django.db.models.functions.datetime.TruncDate("deleted_at"),
                        models.F("deleted_at"),
                        name="deleted_at_date_idx",
                    ),
                ],
            },
        ),
    ]
