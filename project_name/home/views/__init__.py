from .base_novadata_view import BaseNovadataView
from .design_system import design_system
from .errors import error_403, error_404, error_500
from .home import home
from .svg_viewer import svg_viewer

errors_views = [
    error_403,
    error_404,
    error_500,
]

__all__ = [
    BaseNovadataView,
    home,
    design_system,
    svg_viewer,
] + errors_views
