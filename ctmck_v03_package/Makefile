# CTMCK Project Makefile

.PHONY: pdf clean lint help all check

# Default target
all: pdf

# Build PDF
pdf:
	@echo "Building CTMCK article PDF..."
	@./compile_check.sh

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	@rm -rf build_temp/
	@find . -name "*.aux" -delete
	@find . -name "*.log" -delete
	@find . -name "*.out" -delete
	@find . -name "*.toc" -delete
	@find . -name "*.fls" -delete
	@find . -name "*.fdb_latexmk" -delete
	@find . -name "*.synctex.gz" -delete
	@find . -name "*.bbl" -delete
	@find . -name "*.blg" -delete
	@echo "Clean completed."

# Python code quality checks
lint:
	@echo "Running Python linting..."
	@if command -v flake8 >/dev/null 2>&1; then \
		find scripts/ -name "*.py" -exec flake8 {} \; ; \
	else \
		echo "flake8 not found. Install with: pip install flake8"; \
	fi
	@if command -v black >/dev/null 2>&1; then \
		find scripts/ -name "*.py" -exec black --check {} \; ; \
	else \
		echo "black not found. Install with: pip install black"; \
	fi

# Quality checks
check: pdf lint
	@echo "Running all quality checks..."
	@if [ -f docs/ctmck_article_v03.pdf ]; then \
		echo "✓ PDF generated successfully"; \
	else \
		echo "✗ PDF generation failed"; \
		exit 1; \
	fi
	@echo "Quality check completed."

# Help
help:
	@echo "CTMCK Project Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  pdf    - Build the main article PDF"
	@echo "  clean  - Remove build artifacts"
	@echo "  lint   - Run Python code quality checks"
	@echo "  check  - Run all quality checks"
	@echo "  help   - Show this help message"
	@echo ""
	@echo "Example usage:"
	@echo "  make pdf    # Build PDF"
	@echo "  make clean  # Clean artifacts"
	@echo "  make check  # Full quality check"
