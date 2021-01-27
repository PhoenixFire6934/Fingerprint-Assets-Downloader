class CdnUrl:
    def get_url(self, game):
        game = game.replace(' ', '').lower()
        if game == 'boombeach':
            url = 'http://df70a89d32075567ba62-1e50fe9ed7ef652688e6e5fff773074c.r40.cf1.rackcdn.com'
        elif game == 'clashofclans':
            url = 'http://b46f744d64acd2191eda-3720c0374d47e9a0dd52be4d281c260f.r11.cf2.rackcdn.com'
        elif game == 'clashroyale':
            url = 'http://7166046b142482e67b30-2a63f4436c967aa7d355061bd0d924a1.r65.cf1.rackcdn.com'
        elif game == 'brawlstars':
            url = 'http://a678dbc1c015a893c9fd-4e8cc3b1ad3a3c940c504815caefa967.r87.cf2.rackcdn.com'
        elif game == 'hayday':
            url = 'https://c12049120.ssl.cf2.rackcdn.com'
        elif game == 'haydaypop':
            url = 'https://d3br6iao8asuhe.cloudfront.net'
        else:
            print(f"Unsupported game {game}!")
            url = None
        return url