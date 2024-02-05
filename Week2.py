# One aspect of data structures that I would find challenging would be zip()funciton as I've never done it before.
# After reviewing it, a zip() works to create multiple iterables and creating tuples. usually used to combine data from different sources.

# Example usage of zip() with lists
names = ["Johnny", "Frank", "Charles"]
ages = [10, 20, 30]

zipped_data = zip(names, ages)
result_list = list(zipped_data)

print(result_list)
