How to edit an OVS Orbit episode
================================

Important Audacity features
---------------------------

Selection: F1 to switch to the selection tool.  Then click in a track
to select a point in time or click and drag in a track to select a
region of time.  Space to play the region, Del to delete it,
Shift+click to expand it.

Zoom: Ctrl+2 for "normal" zoom, Ctrl+1 to zoom in, Ctrl+3 to zoom 4.
Or use F4 to switch to the Zoom tool and left-click to zoom in there,
right-click to zoom out, or select a region of audio to zoom to that
region.

"Sync-Lock": Use Tracks|Sync-Lock Tracks (or the toolbar item that
looks like a stopwatch) to turn this on or off.  When Sync-Lock is on,
deleting a range of audio deletes it from all the tracks (actually,
from all the tracks not separated from the current one by a Label
track).  When it is off, it deletes it only from the single selected
track.

The left side of the track UI has a relative volume slider that goes
from -25 dB to +36 dB.  It also has Mute and Solo buttons that are
useful for listening to just some of the audio tracks.

Audacity has really good undo/redo with Control+Z and Control+Shift+Z.


Instructions
------------

 1. Collect all of the audio tracks into a Audacity project.

 2. Change the name of each track to reflect the content, e.g. "Ben",
    "Paul" (assuming that's a guest's name), "audience".

 3. If tracks were recorded unsynchronized on separate devices, then
    use the Time Shift Tool (F5) to properly align the tracks (turn
    Sync-Lock off).  Sometimes this is easy because I remembered to
    clap loudly after starting the recording so that you can just line
    up the vertical edge.

 4. Find the real beginning of the episode and delete everything before
    it.  (Make sure Sync-Lock is on.)  You can do this by clicking in
    the right place, typing Shift+J then Del.

 5. Find the real end of the episode and delete everything after it.
    (Make sure Sync-Lock is on.)  You can do this by clicking in the
    right place, typing Shift+K then Del.

 6. Listen to a few seconds of audio from each track individually and
    adjust the track volume sliders so that the tracks are roughly the
    same volume.  Only relative volumes matter: if you have two tracks
    and set them to +0 dB and +10 dB, that's just as good as if you end
    up with +5 dB and +15 dB, since it's a 10-dB difference in both
    cases.  Whatever.

 7. Starting from the beginning of the audio, listen to the entire
    episode.  You have three jobs, described below:

    (a) Delete audio that shouldn't appear in the final episode.  Audio
	to delete includes the following:

	  * Long silences (3+ seconds).

	  * Loud noises like doors slamming or a table being thumped.

	  * Interruptions from people walking into the room.

	  * Bits where people get the conference calls or projector set
	    up.

	  * Very long "ummms" from one speaker or another.

	  * The speaker starting a long thought over.

	  * The speaker saying that he shouldn't have said something he
	    just said.

	  * Worthless bits like "Do you have anything to add?" "No."

	To delete audio, first ensure that Sync-Lock is on, then use
	the Selection tool (F1) to select the audio region to be
	deleted.  Press "c" to listen to the audio on either side of
	the deleted region before you actually delete it (you can
	configure the time in Edit|Preferences... in the Playback tab's
	"Cut Preview" pane).  When you're sure you want to delete it,
	press Del.

    (b) Reduce noise that degrades the audio quality.  If the episode
	was recorded with high-quality microphones, there might not be
	much to delete and you have an easy job.  However, a lot of
	episodes get recorded with one high-quality microphone and one
	lapel mic that tends to be somewhat noisy.  Sometimes there's
	also some echo from one mic to another that is best removed.

	The main strategy for reducing noise is to mute tracks that
	don't need to be on because the person at that mic is not
	speaking.  To do that, with the Selection Tool (F1), select a
	region of audio in which the mic should really be silent, then
	push Control+L.  For some recordings, this makes a big
	difference in quality, although it can be time consuming.

    (c) Write up an episode description.  Start by making a copy of
        fragments/episode-skeleton.xml.  Then, edit it to describe the person
        speaking or being interviewed, what the episode is about, how to
        contact the interviewee, and adding pointers to related episodes (if
        any).  Make sure to credit yourself in the attribution block at the
        end.

        The episode description eventually gets copied directly into the RSS.
        It should only use simple HTML.  Some podcatchers don't render HTML at
        all and just delete all the tags, and some only show paragraph breaks
        if there's a blank line in the input, so make sure there's a blank line
        between </p> and <p> and between </li> and <li>.

 8. Level the volume within each individual track.  Sometimes the
    volume in a given track is pretty constant, if the speaker has
    reasonable discipline about staying a constant distance from the
    microphone.  In such a case, there's nothing to do.  But sometimes
    you get a speaker who wildly moves around the room, or occasionally
    the mic gain gets adjusted on the recorder during recording.  If
    so, probably you noticed that while listening in step 7 (sometimes
    it's obvious from glancing at the track, because the levels sharply
    rise or fall a few minutes into the recording).  Either way, you
    can select the audio region or regions that stand out from the rest
    and use either Effect|Amplify... or the Envelope Tool (F2) to level
    its volume with the rest of the track.  More often, I use Amplify,
    but it's more "permanent" than the Envelope Tool.

    The volume won't be perfectly level.  That's OK.

    If you make any changes, you might need to adjust the track volume
    sliders to keep the tracks at relatively the same volume.

 9. If there isn't already a episode introduction track ("Welcome to
    OVS Orbit, the podcast for..."), then you can record one, if you
    want to and have good equipment for it.  Otherwise skip it for now
    and Ben will add one later.

10. Insert intro.wav, bumper.wav, and outro.wav tracks
    (File|Import|Audio), and add label tracks as Sync-Lock separators
    (Tracks|Add New|Label Track), then drag the tracks vertically to
    reorder them so that you have something like this:

    intro.wav
    episode introduction track (if recorded)
    bumper.wav
    ---Label Track---
    speaker1.wav
    speaker2.wav
    ---Label Track---
    outro.wav

10. Use the Time Shift Tool (F5) to shift the tracks so that they're
    in the right order.  Sync-Lock should be on for shifting the
    tracks that are the main body of the episode, off for shifting the
    others.

11. Compare the levels for intro.wav, bumper.wav, and outro.wav to the
    levels for the other tracks.  Adjust the other tracks so that they
    match.  Usually this is a matter of just moving them up or down
    all the same amount; for example, maybe they all need to be 6-dB
    louder than before.

    Do not adjust the levels for intro.wav, bumper.wav, and outro.wav;
    these should always be +0 dB.  That ensures that every episode has
    the same overall loudness.

12. Save the project; you're done!
