document.addEventListener('DOMContentLoaded', function () {
    // Profile Picture Preview
    const photoInput = document.getElementById('id_photo');
    const profilePreview = document.getElementById('profile-preview');

    if (photoInput) {
        photoInput.addEventListener('change', function () {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    profilePreview.src = e.target.result;
                    profilePreview.style.display = 'block';
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // Flatpickr for Availability Time Selection
    const timeInputs = document.querySelectorAll("input[type='time']");
    if (timeInputs) {
        timeInputs.forEach(function (input) {
            flatpickr(input, {
                enableTime: true,
                noCalendar: true,
                dateFormat: "H:i",
                altInput: true,
                altFormat: "h:i K",
            });
        });
    }

    // Add Dynamic Availability Row
    const addAvailabilityButton = document.getElementById('add-availability');
    const availabilityContainer = document.getElementById('availability-container');
    if (addAvailabilityButton && availabilityContainer) {
        addAvailabilityButton.addEventListener('click', function (e) {
            e.preventDefault();
            const newRow = document.createElement('div');
            newRow.classList.add('row', 'mb-3');
            newRow.innerHTML = `
                <div class="col-md-4">
                    <select name="day" class="form-control">
                        <option value="monday">Monday</option>
                        <option value="tuesday">Tuesday</option>
                        <option value="wednesday">Wednesday</option>
                        <option value="thursday">Thursday</option>
                        <option value="friday">Friday</option>
                        <option value="saturday">Saturday</option>
                        <option value="sunday">Sunday</option>
                    </select>
                </div>
                <div class="col-md-3">
                    <input type="time" name="start_time" class="form-control">
                </div>
                <div class="col-md-3">
                    <input type="time" name="end_time" class="form-control">
                </div>
                <div class="col-md-2">
                    <button class="btn btn-danger remove-availability">Remove</button>
                </div>
            `;
            availabilityContainer.appendChild(newRow);
        });

        // Remove Availability Row
        availabilityContainer.addEventListener('click', function (e) {
            if (e.target && e.target.classList.contains('remove-availability')) {
                e.preventDefault();
                e.target.closest('.row').remove();
            }
        });
    }

    // Form Validation
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function (e) {
            const errors = [];
            const timeFields = document.querySelectorAll("input[type='time']");
            timeFields.forEach(function (field) {
                if (!field.value) {
                    errors.push("Time fields cannot be empty.");
                    field.classList.add('is-invalid');
                } else {
                    field.classList.remove('is-invalid');
                }
            });

            const photoInput = document.getElementById('id_photo');
            if (photoInput && photoInput.files[0]) {
                const file = photoInput.files[0];
                const maxSize = 2 * 1024 * 1024; // 2 MB
                if (file.size > maxSize) {
                    errors.push("Profile picture must be less than 2MB.");
                    photoInput.classList.add('is-invalid');
                } else {
                    photoInput.classList.remove('is-invalid');
                }
            }

            if (errors.length > 0) {
                e.preventDefault();
                alert("Please fix the following errors:\n" + errors.join("\n"));
            }
        });
    }
});
