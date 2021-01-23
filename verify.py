import hashlib, hmac, base64
api_key=API_KEY;
event_time="1588705971";
event_type="signature_request_sent";
json='{"event":{"event_type":"signature_request_sent","event_time":"1588705971","event_hash":"722841562d76e2eebd94dcad4c5751afbef4be01345357b2f8523278470874ef","event_metadata":{"related_signature_id":null,"reported_for_account_id":null,"reported_for_app_id":"fe56f31389ffaf8eea2c55ddd05912db"}},"email_addresses":[],"template_ids":null}}';

def verify_event_hash( api_key,event_time,event_type):
    #hash=hmac.new(api_key, ('1580433891template_created'), hashlib.sha256).hexdigest();
    hash=hmac.new(api_key, (event_time+event_type), hashlib.sha256).hexdigest();
    print hash
    return

verify_event_hash(api_key,event_time,event_type);


def check_header(json, api_key):
    encoded = base64.b64encode(hmac.new(api_key, json, hashlib.md5).hexdigest())
    return encoded

print check_header(json, api_key)
