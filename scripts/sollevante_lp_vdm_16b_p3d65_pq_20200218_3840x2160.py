import xml.etree.ElementTree as ET
import opentimelineio as otio

tree = ET.parse('sollevante_lp_16b_hdr_p3d65pq_dolbyvision29.xml')
root = tree.getroot()

timeline = otio.schema.Timeline(name="Sol Levante")
track = otio.schema.Track(name="Main Layer", kind="Video")
timeline.tracks.append(track)

rate = 24
for child in root[2][0][4][0]:
    if 'Shot' == child.tag:
        for child2 in child:
            if 'Record' == child2.tag:
                clip = otio.schema.Clip(source_range=otio.opentime.TimeRange(
                    otio.opentime.RationalTime(int(child2[0].text), rate),
                    otio.opentime.RationalTime(int(child2[1].text), rate)))
                clip.media_reference = otio.schema.ImageSequenceReference()
                clip.media_reference.target_url_base = ""
                clip.media_reference.name_prefix = "sollevante_lp_vdm_16b_p3d65_pq_20200218_3840x2160."
                clip.media_reference.name_suffix = ".tiff"
                clip.media_reference.start_frame = 0
                clip.media_reference.frame_step = 1
                clip.media_reference.rate = rate
                clip.media_reference.frame_zero_padding = 7
                track.append(clip)

otio.adapters.write_to_file(timeline, 'sollevante_lp_vdm_16b_p3d65_pq_20200218_3840x2160.otio')
