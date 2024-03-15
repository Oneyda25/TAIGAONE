/**
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 *
 * Copyright (c) 2023-present Kaleidos INC
 */
export interface Schema {
    name: string;
    path?: string;
    project?: string;
    module?: string;
    globalState: string;
    localState: string;
}