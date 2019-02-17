import level
import thingspeak
channel_id ="340326"
write_key  ="Z8UH5I7G37I3VOKM"
read_key ="XRF157M66Y761Z78"
def uploaddata(level):
    channel = thingspeak.Channel(id=channel_id,write_key=write_key)
    try:
        response = channel.update({1:level})
    except:
        print ("connection failed")
