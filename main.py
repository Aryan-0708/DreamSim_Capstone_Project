import sys
import subprocess
import time
from agents import agent_vision, agent_artist, agent_engineer, agent_qa

def main():
    print("=======================================")
    print("   🎮 DreamSim: 4-Agent Game Gen 🎮   ")
    print("=======================================")
    
    # 1. Get Input
    if len(sys.argv) > 1:
        user_prompt = " ".join(sys.argv[1:])
    else:
        user_prompt = input("\nDescribe your dream game: ")

    start_time = time.time()

    # 2. Vision Agent
    design_json = agent_vision(user_prompt)
    print(f"\n📄 GDD Generated (Size: {len(design_json)} chars)")

    # 3. Artist Agent
    artist_code = agent_artist(design_json)
    print(f"🖼️  Assets Created (Lines: {len(artist_code.splitlines())})")

    # 4. Engineer Agent
    raw_code = agent_engineer(design_json, artist_code)
    print(f"💻 Logic Written (Lines: {len(raw_code.splitlines())})")

    # 5. QA Agent
    final_code = agent_qa(raw_code)
    
    # 6. Save & Launch
    filename = "dream_game.py"
    with open(filename, "w") as f:
        f.write(final_code)
    
    end_time = time.time()
    print(f"\n✨ Game Ready in {round(end_time - start_time, 2)} seconds!")
    print(f"🚀 Launching {filename}...\n")
    
    try:
        subprocess.run([sys.executable, filename])
    except KeyboardInterrupt:
        print("\n👋 Thanks for playing!")

if __name__ == "__main__":
    main()