#!/usr/bin/env python
# encoding: utf-8
#
# Copyright © 2019, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from .service import Service


class MLPipelineAutomation(Service):
    """Automates project creation, pipeline building and training.

    The Machine Learning Pipeline Automation (MLPA) API enables CRUD operations
    on automation projects, which automates VDMML project creation, pipeline
    building and training, and the production of champion models.
    """

    _SERVICE_ROOT = '/mlPipelineAutomation'

    list_projects, get_project, update_project, \
    delete_project = Service._crud_funcs('/projects', 'project')

    @classmethod
    def create_project(cls, table, target, name, description=None,
                       max_models=None):
        """Create a new pipeline automation project.

        Parameters
        ----------
        table : str
            URI of the input data table (as returned by `data_sources` service.
        target : str
            Name of column in `table` containing the target variable.
        name : str
            Name of the project.
        description : str, optional
            A description of the project.
        max_models : int, optional
            Maximum number of models to train.
        """

        data = {
            'dataTableUri': table,
            'description': description,
            'name': name,
            'type': 'predictive',
            'analyticsProjectAttributes': {
                'targetVariable': target
            },
            'settings': {

            },
            'version': 1
        }

        if max_models is not None:
            data['settings']['numberOfModels'] = int(max_models)

        """
        projectAttributes
            target event level
            class selection statistic
            interval selection statistic
            partition enabled
        
        settings
            autorun
            
        buildMethod: str
        """

        r = cls.post('/projects',
                     headers={
                         'Content-Type':
                             'application/vnd.sas.analytics.ml.pipeline.automation.project+json',
                         'Accept':
                             'application/vnd.sas.analytics.ml.pipeline.automation.project+json'},
                     json=data
                     )

        return r
