```bash
docker-compose up -d
docker-compose exec artemis /var/lib/artemis-instance/bin/artemis queue create --address="VirtualTopic.Orders" --name="Consumer.VirtualTopic.Orders" --user=admin --password="password" --preserve-on-no-consumers --durable --multicast --auto-create-address=True
```