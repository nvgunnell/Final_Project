from tethys_sdk.base import TethysAppBase, url_map_maker


class FinalProject(TethysAppBase):
    """
    Tethys app class for Final Project.
    """

    name = 'Final Project'
    index = 'final_project:home'
    icon = 'final_project/images/icon.gif'
    package = 'final_project'
    root_url = 'final-project'
    color = '#d35400'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='final-project',
                controller='final_project.controllers.home'
            ),
        )

        return url_maps