#!/usr/bin/env ruby
#
# Set each post's latest committed timestamp

Jekyll::Hooks.register :posts, :post_init do |post|
  lastmod_date = `git log -1 --pretty="%ad" --date=iso -- "#{ post.path }"`.strip

  unless lastmod_date.empty?
    post.data['last_modified_at'] = lastmod_date
  end
end
