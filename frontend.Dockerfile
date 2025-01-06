FROM node:18
RUN yarn config set registry https://registry.npmmirror.com/
COPY frontend/package.json /package.json
COPY frontend/yarn.lock /yarn.lock

# it's not entirely clear what --modules-folder does. It probably works without.
# the general idea is that the /node_modules are outside the volume mount into /app which
# later happens (see docker-compose.yml -> frontend service)
RUN yarn install --pure-lockfile --modules-folder /node_modules
