class BattlePersistentMusic():
    sound_type = ['calm', 'encntr', 'limit']
    PLACEHOLDER_VOLUME = 0.9

    def __init__(self,
                 calm='phase_7/audio/bgm/encntr_infinity.ogg', encntr='phase_7/audio/bgm/encntr_infinity.ogg',
                 limit='phase_7/audio/bgm/encntr_infinity_boss.ogg'):
        self.track_variants = [0, 0, 0]
        self.track_paths = [calm, encntr, limit]
        for x in range(len(self.track_variants)):
            self.track_variants[x] = base.loader.loadMusic(self.track_paths[x])

    def play(self, type='calm'):
        for x in self.track_variants:
            base.playMusic(x, looping=1, volume=0)
        for x, y in zip(self.sound_type, self.track_variants):
            if type == x:
                y.setVolume(self.PLACEHOLDER_VOLUME)
                break

    def switchMode(self, type='encntr'):
        for x, y in zip(self.track_variants, self.sound_type):
            new_volume = 0
            if type == y:
                new_volume = self.PLACEHOLDER_VOLUME
            x.setVolume(new_volume)

    def unload(self):
        for x in self.track_variants:
            x.stop()
