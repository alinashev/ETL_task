class Metadata:
    browser = None
    platform = None
    date_land = None
    date_submit = None
    user_agent = None
    referer = None
    network_id = None

    def __init__(self, browser, platform, date_land, date_submit, user_agent, referer, network_id):
        self.browser = browser
        self.platform = platform
        self.date_land = date_land
        self.date_submit = date_submit
        self.user_agent = user_agent
        self.referer = referer
        self.network_id = network_id

    def __str__(self) -> str:
        return 'browser{browser} ' \
               '\nplatform{platform} ' \
               '\ndate_land{date_land} ' \
               '\ndate_submit{date_submit} ' \
               '\nuser_agent{user_agent} ' \
               '\nreferer{referer} ' \
               '\nnetwork_id{network_id} \n'.format(browser=self.browser,
                                                    platform=self.platform,
                                                    date_land=self.date_land,
                                                    date_submit=self.date_submit,
                                                    user_agent=self.user_agent,
                                                    referer=self.referer,
                                                    network_id=self.network_id)
