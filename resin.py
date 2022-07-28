import asyncio
import genshin
import os

async def main():
    ltuid = your_hoyolab_uid
    ltoken = "your_ltoken"
    uid = your_genshin_uid
    cookies = {"ltuid": ltuid, "ltoken": ltoken}
    client = genshin.GenshinClient(cookies)
    notes = await client.get_notes(uid)
    print(f"Resin: {notes.current_resin}/{notes.max_resin}")
    print((((160-notes.current_resin)/0.125)/60) ,"hour(s) until cap")
    os.system("pause")
    await client.close()
asyncio.run(main())
