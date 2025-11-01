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

    _operational_variables = ["p", "rnr10", "rro10", "rsu", "rre"]

    def get_bounds_pu(self, attr: str) -> tuple[xr.DataArray, xr.DataArray]:
        """Get per unit bounds for generators.

        <!-- md:badge-version v1.0.0 -->

        Parameters
        ----------
        attr : string, optional
            Attribute name for the bounds, e.g. "p", "rnr10", "rro10", "rsu", "rre"

        Returns
        -------
        tuple[xr.DataArray, xr.DataArray]
            Tuple of (min_pu, max_pu) DataArrays.

        """
        if attr not in self._operational_variables:
            msg = (
                f"Bounds can only be retrieved for operational attributes. "
                f"For generators those are: {', '.join(self._operational_variables)}."
            )
            raise ValueError(msg)

        # Construir los nombres de los bounds dinámicamente
        min_key = f"{attr}_min_pu"
        max_key = f"{attr}_max_pu"

        # Si no existen columnas específicas, usar las de p por defecto
        if not hasattr(self.da, min_key):
            min_pu = self.da.p_min_pu
            max_pu = self.da.p_max_pu
        else:
            min_pu = getattr(self.da, min_key)
            max_pu = getattr(self.da, max_key)

        return min_pu, max_pu

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
