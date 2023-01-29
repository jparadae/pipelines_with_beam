import apache_beam as beam

with beam.Pipeline() as p:
  samples_per_key = (
      p
      | 'Create produce' >> beam.Create([
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
      | 'Samples per key' >> beam.combiners.Sample.FixedSizePerKey(6)
      | beam.Map(print))
  
# Results Excec
#('spring', ['🍆', '🥕', '🍅', '🍓'])
#('summer', ['🌽', '🍅', '🥕'])
#('fall', ['🥕', '🍅'])
#('winter', ['🍆'])
      