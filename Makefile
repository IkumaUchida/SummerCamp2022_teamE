.PHONY: docker
docker:
	docker build -t summer_camp:latest .
	docker run --gpus all --rm -t summer_camp:latest  nvidia-smi
	docker run --rm -t summer_camp:latest echo "summer_camp done"

.PHONY: docker-run
docker-run:
	docker run \
	--name summer_camp \
	--gpus all \
	-d \
	-u $(id -u):$(id -g) \
	--shm-size=8G \
	-it \
	-v $(PWD):/workspace \
	summer_camp:latest

	docker attach summer_camp


.PHONY: docker-rm
docker-rm:
	docker rm summer_camp