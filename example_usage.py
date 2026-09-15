import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import MultimodalAudioEmotionValenceDetectorClient

def main():
    client = MultimodalAudioEmotionValenceDetectorClient()
    res = client.detect_audio_emotion()
    print("=== Multimodal Audio Emotion Valence Detector Output ===")
    print(f"Valence: {res['emotional_valence_score']} | Arousal: {res['acoustic_arousal_score']}")
    print(f"Frustration Detected: {res['frustration_detected']}")
    print(f"Agent Persona Adaptation: {res['recommended_agent_persona_adaptation']}")
    print(f"Barge-in Priority Boost: {res['barge_in_priority_boost']}")

if __name__ == '__main__':
    main()
