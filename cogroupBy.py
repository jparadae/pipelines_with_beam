import apache_beam as beam

#Declare pipeline of data
with beam.Pipeline() as p:
  total = (
      p
      | 'Create vegetables counts' >> beam.Create([
          ('🥕', 3),
          ('🥕', 2),
          ('🍆', 1),
          ('🍅', 4),
          ('🍅', 5),
          ('🍅', 3),
      ])
      | 'Sum' >> beam.CombinePerKey(sum)
      | beam.Map(print))

# Results excecution
# ('🥕', 5)
#('🍆', 1)
#('🍅', 12)
