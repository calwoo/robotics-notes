FROM ruby:3.1.0

EXPOSE 3000

RUN gem install bundler:2.3.3

COPY Gemfile* ./
RUN bundle install

COPY . .

RUN rails db:migrate RAILS_ENV=production
RUN rake assets:precompile

WORKDIR /usr/src/app

CMD ["rails", "s", "-e", "production"]
