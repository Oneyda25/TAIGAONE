# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2023-present Kaleidos INC

# Generated by Django 4.1.3 on 2023-06-12 18:57

import django.db.models.deletion
import taiga.base.db.models
import taiga.base.db.models.fields
import taiga.base.utils.datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0001_initial"),
        ("projects_roles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectInvitation",
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
                    models.DateTimeField(default=taiga.base.utils.datetime.aware_utcnow, verbose_name="created at"),
                ),
                ("email", taiga.base.db.models.fields.LowerEmailField(max_length=255, verbose_name="email")),
                (
                    "status",
                    models.CharField(
                        choices=[("pending", "Pending"), ("accepted", "Accepted"), ("revoked", "Revoked")],
                        default="pending",
                        max_length=50,
                        verbose_name="status",
                    ),
                ),
                ("num_emails_sent", models.IntegerField(default=1, verbose_name="num emails sent")),
                ("resent_at", models.DateTimeField(blank=True, null=True, verbose_name="resent at")),
                ("revoked_at", models.DateTimeField(blank=True, null=True, verbose_name="revoked at")),
                (
                    "invited_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="ihaveinvited+",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="invited by",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invitations",
                        to="projects.project",
                        verbose_name="project",
                    ),
                ),
                (
                    "resent_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="ihaveresent+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "revoked_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="ihaverevoked+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invitations",
                        to="projects_roles.projectrole",
                        verbose_name="role",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_invitations",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "project invitation",
                "verbose_name_plural": "project invitations",
                "ordering": ["project", "user", "email"],
            },
        ),
        migrations.AddIndex(
            model_name="projectinvitation",
            index=models.Index(fields=["email"], name="projects_in_email_07fdb9_idx"),
        ),
        migrations.AddIndex(
            model_name="projectinvitation",
            index=models.Index(fields=["project", "email"], name="projects_in_project_d7d2d6_idx"),
        ),
        migrations.AddIndex(
            model_name="projectinvitation",
            index=models.Index(fields=["project", "user"], name="projects_in_project_ac92b3_idx"),
        ),
        migrations.AddConstraint(
            model_name="projectinvitation",
            constraint=models.UniqueConstraint(
                fields=("project", "email"), name="projects_invitations_projectinvitation_unique_project_email"
            ),
        ),
    ]