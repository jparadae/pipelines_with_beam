import apache_beam as beam

with beam.Pipeline() as p:
  icon_pairs = p | 'Create icons' >> beam.Create([
      ('Apple', '🍎'),
      ('Apple', '🍏'),
      ('Eggplant', '🍆'),
      ('Tomato', '🍅'),
  ])

  duration_pairs = p | 'Create durations' >> beam.Create([
      ('Apple', 'perennial'),
      ('Carrot', 'biennial'),
      ('Tomato', 'perennial'),
      ('Tomato', 'annual'),
  ])

  plants = (({
      'icons': icon_pairs, 'durations': duration_pairs
  })
            | 'Merge' >> beam.CoGroupByKey()
            | beam.Map(print))
  
  #Results
#('Apple', {'icons': ['🍎', '🍏'], 'durations': ['perennial']})
#('Eggplant', {'icons': ['🍆'], 'durations': []})
#('Tomato', {'icons': ['🍅'], 'durations': ['perennial', 'annual']})
#('Carrot', {'icons': [], 'durations': ['biennial']})