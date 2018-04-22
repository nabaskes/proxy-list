from countries import Countries


class Proxy(object):
    def __init__(self,
                 filtermode='strict',
                 countries=None,
                 countriesBlackList=None,
                 protocols=['http', 'https'],
                 anonymityLevels=['anonymous', 'elite'],
                 sourcesWhiteList=None,
                 series=False,
                 ipTypes=['ipv4'],
                 defaultRequestOptions=None):
        self._protocols = ['http', 'https', 'socks4', 'socks5']
        self._anonymityLevels = ['transparent', 'anonymous', 'elite']
        self._countries = Countries
        self._sources = ['bitproxies',
                         'blackhatworld',
                         'coolproxy',
                         'freeproxylist',
                         'freeproxylists',
                         'gatherproxy',
                         'incloak',
                         'kingproxies',
                         'premproxy',
                         'proxies24',
                         'proxydb',
                         'proxylisten',
                         'sockslist']
        self._iptypes = ['ipv4', 'ipv6']



    def getProxies(self, options):
        sources = self._sources
        # asyncmethod = 'eachSeries' if options.series else 'each'
