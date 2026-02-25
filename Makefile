HUGO := /home/parkjunwoo/bin/hugo

.PHONY: serve build clean deploy

serve:
	$(HUGO) server -D

build:
	$(HUGO) --minify

clean:
	rm -rf public/

deploy: build
	aws s3 sync public/ s3://dabel5-public/ --delete --exact-timestamps
	aws s3 cp s3://dabel5-public/ s3://dabel5-public/ --recursive --exclude "*" --include "*.xml" --content-type "application/xml; charset=utf-8" --metadata-directive REPLACE
	aws cloudfront create-invalidation --distribution-id E1Y9CPCZ1N74HX --paths "/*"
