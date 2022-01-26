
server-version staff-build-1.0
model-path resources
dc-file etc/toon.dc
dc-file etc/otp.dc
window-title Toontown: Event Horizon

icon-filename phase_3/models/gui/toontown.ico
load-display pandadx9
aux-display pandagl
aux-display pandadx9
aux-display tinydisplay
default-directnotify-level info
notify-level-collide warning
notify-level-chan warning
notify-level-gobj warning
notify-level-loader warning
notify-timestamp #t
notify-integrate #f
default-model-extension .bam
audio-library-name p3openal_audio
cursor-filename phase_3/models/gui/toonmono.cur

want-dev 1
schellgames-dev 0
want-magic-words #t
want-code-redemption-init-db true
support-rename 1
teleport-all 0 //disable during production
want-cogdominiums #t

is-winter-running #f
