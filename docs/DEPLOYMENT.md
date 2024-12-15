
# Deployment Guide

## Development Environment

1. Clone the repository in Replit
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure environment variables in Replit Secrets:
   ```
   DATABASE_URL=postgresql://username:password@host:5432/dbname
   SECRET_KEY=your-secret-key
   DEBUG=True
   ```

4. Run development server:
   ```
   python app/main.py
   ```
   Server runs on port 5001

## Production Deployment

1. Use Replit's Deployment feature:
   - Click "Deploy" in the top bar
   - Choose "Production" environment

2. Configure Production Settings:
   - Resources: 1 vCPU, 2 GiB RAM
   - Autoscaling: Enable
   - Domain: Set custom domain if needed

3. Set Production Environment:
   ```
   DATABASE_URL=postgresql://prod_user:prod_pass@host:5432/prod_db
   SECRET_KEY=production-secret-key
   DEBUG=False
   ```

4. Deploy:
   - Click "Deploy"
   - Replit handles SSL, scaling, and monitoring

## Monitoring

1. View Metrics:
   - CPU/Memory usage
   - Request latency
   - Error rates

2. Access Logs:
   - Application logs
   - System metrics
   - Request tracking

## Maintenance

1. Updates:
   - Push code changes
   - Click "Deploy" to update
   - Zero-downtime deployment

2. Database Backups:
   - Automated backups
   - Point-in-time recovery

## Security

1. SSL/TLS encryption (automatic)
2. DDoS protection
3. Regular security updates
4. Access control management

## Troubleshooting

1. Check deployment logs
2. Verify environment variables
3. Monitor resource usage
4. Check database connectivity
