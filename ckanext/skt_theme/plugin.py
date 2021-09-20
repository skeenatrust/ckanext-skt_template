from ckan import plugins
from ckan.plugins import toolkit


class SKTThemePlugin(plugins.SingletonPlugin):
    '''SKT Theme
    '''
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
