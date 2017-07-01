from beautifulhue.api import Bridge
import secret_keys

bridge = Bridge(device={'ip':secret_keys.hue_ip}, user={'name':secret_keys.hue_key})
lights = bridge.light.get({'which':'all'})


def get_light_by_name(name):
    for light in lights['resource']:
        if light['name']==name:
            return light


def toggle_light(light, toggle_state ):
    resource = {
        'which':light['id'],
        'data':{
            'state':{'on':toggle_state, 'effect':'none'}
        }
    }
    bridge.light.update(resource)



