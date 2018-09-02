import time
import asyncio

"""
it has taken 8 seconds for 
50008000, 1000
76500, 150
500, 30
TOOK 16.516292572021484s
"""


async def find_divisibles(inrange, div_by):
    print("Finding numbers in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.001)

    print("Done CHECKING FOR RANGE {}".format(inrange))
    return located


async def main():
    divs1 = loop.create_task(find_divisibles(50008000, 1000))
    divs2 = loop.create_task(find_divisibles(765000, 150))
    divs3 = loop.create_task(find_divisibles(500, 30))
    await asyncio.wait([divs1, divs2, divs3])
    # MUST DO ELSE TASKS gets dispatched without ever returning
    return divs1, divs2, divs3

if __name__ == "__main__":
    try:
        start = time.time()
        loop = asyncio.get_event_loop()
        div1, div2, div3 = loop.run_until_complete(main())  # These are rerults objects not the actual lists.
        print(div2.result())  # To get the actual result value
        end = time.time()
        print("TOOK {}s".format(end-start))
    except Exception as e:
        print("La la lala")
    finally:
        loop.close()