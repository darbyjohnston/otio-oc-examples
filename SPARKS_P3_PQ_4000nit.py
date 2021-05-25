import xml.etree.ElementTree as ET
import opentimelineio as otio

tree = ET.parse('20161103_SPARKS_DOVI_METADATA_AR_CORRECT.xml')
root = tree.getroot()

timeline = otio.schema.Timeline(name="Sol Levante")
track = otio.schema.Track(name="V1", kind="Video")
timeline.tracks.append(track)

rate = 59.94005994005994
for child in root[1][0][5][0]:
    if 'Shot' == child.tag:
        for child2 in child:
            if 'Record' == child2.tag:
                clip = otio.schema.Clip(source_range=otio.opentime.TimeRange(
                    otio.opentime.RationalTime(int(child2[0].text), rate),
                    otio.opentime.RationalTime(int(child2[1].text), rate)))
                clip.media_reference = otio.schema.ImageSequenceReference()
                clip.media_reference.target_url_base = ""
                clip.media_reference.name_prefix = "SPARKS_P3_PQ_4000nit_"
                clip.media_reference.name_suffix = ".exr"
                clip.media_reference.start_frame = 0
                clip.media_reference.frame_step = 1
                clip.media_reference.rate = rate
                clip.media_reference.frame_zero_padding = 5
                track.append(clip)

otio.adapters.write_to_file(timeline, 'SPARKS_P3_PQ_4000nit.otio')
