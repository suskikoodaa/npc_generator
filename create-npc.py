from openai import OpenAI
from npc import NPC

client = OpenAI()

region = "Numenor"
room = "Tavern"

def generate_npc(region, room):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a fantasy npc generator."},
            {"role": "user", "content": "region=Shire from Lord of the Rings, room=Bilbo's house"},
            {"role": "assistant", "content": "name=Frodo\nrace=hobbit\nage=60\nwearing=green elven cloak\nwielding=Sting the Elven dagger"},
            {"role": "user", "content": f"region={region}, room={room}"}
        ]
    )
    npc_data = response.choices[0].message.content.split('\n')
    npc = NPC(*[data.split('=')[1] for data in npc_data])
    npc.save_to_file()
    return npc

def main():
  print(generate_npc(region=region, room=room))


if __name__ == "__main__":
  main()
