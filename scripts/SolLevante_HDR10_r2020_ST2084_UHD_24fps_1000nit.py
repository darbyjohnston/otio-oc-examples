import xml.etree.ElementTree as ET
import opentimelineio as otio

tree = ET.parse('sollevante_lp_16b_hdr_p3d65pq_dolbyvision29.xml')
root = tree.getroot()

timeline = otio.schema.Timeline(name="Sol Levante")
track = otio.schema.Track(name="Main Layer", kind="Video")
timeline.tracks.append(track)

for child in root[2][0][4][0]:
    if 'Shot' == child.tag:
        for child2 in child:
            if 'Record' == child2.tag:
                clip = otio.schema.Clip(source_range=otio.opentime.TimeRange(
                    otio.opentime.RationalTime(int(child2[0].text), 24),
                    otio.opentime.RationalTime(int(child2[1].text), 24)))
                clip.media_reference = otio.schema.ExternalReference()
                clip.media_reference.target_url = "SolLevante_HDR10_r2020_ST2084_UHD_24fps_1000nit.mov"
                track.append(clip)

otio.adapters.write_to_file(timeline, 'SolLevante_HDR10_r2020_ST2084_UHD_24fps_1000nit.otio')
