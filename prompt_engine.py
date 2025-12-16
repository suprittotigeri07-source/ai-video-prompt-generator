def generate_video_prompt(brand, product, platform, tone):
    scenes = []

    scenes.append({
        "scene": 1,
        "description": f"Opening hook showing the problem that {product} solves.",
        "visual": "Close-up shot, fast cuts, engaging motion",
        "tone": tone,
        "platform": platform
    })

    scenes.append({
        "scene": 2,
        "description": f"Introduce {brand}'s {product} with clear visuals and benefits.",
        "visual": "Medium shots, smooth transitions, product highlight",
        "tone": tone,
        "platform": platform
    })

    scenes.append({
        "scene": 3,
        "description": "Show social proof or key feature in action.",
        "visual": "User interaction, natural lighting",
        "tone": tone,
        "platform": platform
    })

    scenes.append({
        "scene": 4,
        "description": "Strong call-to-action encouraging users to try the product.",
        "visual": "Bold text overlay, brand colors, logo outro",
        "tone": tone,
        "platform": platform
    })

    return scenes
