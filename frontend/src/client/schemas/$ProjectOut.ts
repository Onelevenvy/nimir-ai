/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export const $ProjectOut = {
    properties: {
        name: {
            type: 'string',
            isRequired: true,
        },
        description: {
            type: 'any-of',
            contains: [{
                type: 'string',
            }, {
                type: 'null',
            }],
        },
        data_dir: {
            type: 'string',
            isRequired: true,
        },
        project_id: {
            type: 'number',
            isRequired: true,
        },
        task_category_id: {
            type: 'any-of',
            contains: [{
                type: 'number',
            }, {
                type: 'null',
            }],
        },
        created: {
            type: 'string',
            isRequired: true,
            format: 'date-time',
        },
        modified: {
            type: 'string',
            isRequired: true,
            format: 'date-time',
        },
    },
} as const;
