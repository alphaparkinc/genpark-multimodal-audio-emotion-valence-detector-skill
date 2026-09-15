import json, sys
from client import MultimodalAudioEmotionValenceDetectorClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "audio-emotion-valence", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "detect_audio_emotion", "description": "Detects customer emotional valence and vocal frustration from speech prosody."}]}}
    elif method == "tools/call":
        client = MultimodalAudioEmotionValenceDetectorClient()
        res = client.detect_audio_emotion()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = MultimodalAudioEmotionValenceDetectorClient()
        print(json.dumps(client.detect_audio_emotion(), indent=2))
