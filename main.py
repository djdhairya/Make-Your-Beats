# description: 
from earsketch import *

setTempo(120)
sounds=[EIGHT_BIT_ATARI_SINEDOT_001,EIGHT_BIT_ATARI_SINEDOT_002,EIGHT_BIT_ATARI_SINEDOT_003,EIGHT_BIT_ATARI_SYNTH_001,EIGHT_BIT_ATARI_SYNTH_002,EIGHT_BIT_ATARI_SYNTH_003,EIGHT_BIT_ATARI_SYNTH_004,EIGHT_BIT_ATARI_SYNTH_005,EIGHT_BIT_ANALOG_DRUM_LOOP_005]
fitMedia(sounds[0], 1, 1, 3)
fitMedia(sounds[1], 2, 3, 6)
fitMedia(sounds[2], 3, 6, 9)
fitMedia(sounds[3], 4, 9, 11)
fitMedia(sounds[4], 5, 11, 14)
fitMedia(sounds[5], 6, 14, 17)
fitMedia(sounds[6], 7, 17, 20)
fitMedia(sounds[7], 8, 20, 23)
fitMedia(sounds[8], 9, 1, 23)

finish()