# SPDX-FileCopyrightText: PyPSA Contributors
#
# SPDX-License-Identifier: MIT

"""Generators components module."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

import pandas as pd

from pypsa.components._types._patch import patch_add_docstring
from pypsa.components.components import Components

if TYPE_CHECKING:
    from collections.abc import Sequence

    import pandas as pd
    import xarray as xr


@patch_add_docstring
class Generators(Components):
    """Generators components class.

    This class is used for generator components. All functionality specific to
    generators is implemented here. Functionality for all components is implemented in
    the abstract base class.

    See Also
    --------
    [pypsa.Components][]

    Examples
    --------
    >>> n.components.generators
    'Generator' Components
    ----------------------
    Attached to PyPSA Network 'AC-DC-Meshed'
    Components: 6

    """

    _operational_variables = ["p", "r"]

    def get_bounds_pu(self, attr: str = "p") -> tuple[xr.DataArray, xr.DataArray]:
        """Get per unit bounds for generators.

        <!-- md:badge-version v1.2.0 -->

        Parameters
        ----------
        attr : string, optional
            Attribute name for the bounds, e.g. "p" or "r".

        Returns
        -------
        tuple[xr.DataArray, xr.DataArray]
            Tuple of (min_pu, max_pu) DataArrays.

        """
        if attr not in self._operational_variables:
            attr = "p"

        min_attr = f"{attr}_min_pu"
        max_attr = f"{attr}_max_pu"

        return getattr(self.da, min_attr), getattr(self.da, max_attr)

    def add(
        self,
        name: str | int | Sequence[int | str],
        suffix: str = "",
        overwrite: bool = False,
        return_names: bool | None = None,
        **kwargs: Any,
    ) -> pd.Index | None:
        """Wrap Components.add() and docstring is patched via decorator."""
        return super().add(
            name=name,
            suffix=suffix,
            overwrite=overwrite,
            return_names=return_names,
            **kwargs,
        )
