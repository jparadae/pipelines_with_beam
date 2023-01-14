
import apache_beam as beam

with beam.Pipeline() as p:
  produce_counts = (
      p
      | 'Create produce counts' >> beam.Create([
          ('spring', '🍓'),
          ('spring', '🥕'),
          ('spring', '🍆'),
          ('spring', '🍅'),
          ('summer', '🥕'),
          ('summer', '🍅'),
          ('summer', '🌽'),
          ('fall', '🥕'),
          ('fall', '🍅'),
          ('winter', '🍆'),
      ])
      | 'Group counts per produce' >> beam.GroupByKey()
      | beam.MapTuple(lambda k, vs: (k, sorted(vs)))  # sort and format
      | beam.Map(print))