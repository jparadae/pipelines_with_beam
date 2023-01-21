import apache_beam as beam

with beam.Pipeline() as p:
  common_items_with_exceptions = (
      p
      | 'Create produce' >> beam.Create([
          {'🍓', '🥕', '🍌', '🍅', '🌶️'},
          {'🍇', '🥕', '🥝', '🍅', '🥔'},
          {'🍉', '🥕', '🍆', '🍅', '🍍'},
          {'🥑', '🥕', '🌽', '🍅', '🥥'},
      ])
      | 'Get common items with exceptions' >> beam.CombineGlobally(
          lambda sets, exclude: \
              set.intersection(*(sets or [set()])) - exclude,
          exclude={'🥕'})
      | beam.Map(print)
  )
#Results
#{'🍅'}