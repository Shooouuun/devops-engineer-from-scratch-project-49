run:
	uv run brain-games

install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

build:
	uv build

package-install:
	uv tool install dist/*.whl

reinstallation: 
	uv tool install --force dist/brain_games-0.1.0-py3-none-any.whl

lint:
	uv run ruff check brain_games

lint--fix:
	uv run ruff check --fix brain_games